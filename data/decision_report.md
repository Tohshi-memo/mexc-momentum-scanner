# Decision Report

- generated_at: 2026-06-10T20:35:31.431454+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6261**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6261, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.41% | **-0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.77% | **+0.27%** |
| ASK | 20/20 | 100.0% | +0.26% | **+0.26%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.17% | **+0.09%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.06% | **+1.06%** |
| MARKET_LONG | 20/20 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.72% | **+0.21%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +0.17% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.73** / 初期 $100.00 (+49.73%)
- 確定: 1247件 (Win 310 / Loss 388 / Flat 549) / skip 1575件
- 成長率目線: 平均log +0.000324 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $149.73

## 4. Latest Market Context

- 更新: 2026-06-10T20:35:25.273207+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=61885.3
- Funnel: target 785 → liquid 154 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.1 >= 65=1, 4h RSI 81.9 >= 65=1, 4h RSI 72.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +67.24% | $26,810,725.65 |
| BEAT/USDT:USDT | +28.60% | $138,359,139.70 |
| JCT/USDT:USDT | +15.12% | $2,214,402.51 |
| STRAX/USDT:USDT | +5.99% | $1,210,031.41 |
| UAI/USDT:USDT | +5.36% | $2,197,711.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STRAX/USDT:USDT | below_1h_threshold | +3.34% | +3.38% |
| FOLKS/USDT:USDT | below_1h_threshold | +3.22% | +3.25% |
| HMSTR/USDT:USDT | below_1h_threshold | +2.95% | +2.99% |
| BSB/USDT:USDT | below_1h_threshold | +1.78% | +1.82% |
| UB/USDT:USDT | below_1h_threshold | +1.69% | +1.72% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
