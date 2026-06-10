# Decision Report

- generated_at: 2026-06-10T20:29:10.187721+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6260**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6260, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.06% | **-0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| ASK | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.77% | **+0.27%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.08% | **+0.04%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.65% | **+0.65%** |
| MARKET_LONG | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.72% | **+0.21%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.32% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.98** / 初期 $100.00 (+48.98%)
- 確定: 1246件 (Win 309 / Loss 388 / Flat 549) / skip 1575件
- 成長率目線: 平均log +0.000320 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STRAX/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $148.98

## 4. Latest Market Context

- 更新: 2026-06-10T20:29:04.065296+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=61858.5
- Funnel: target 785 → liquid 153 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.0 >= 65=1, 4h RSI 81.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +67.89% | $25,840,783.24 |
| BEAT/USDT:USDT | +28.67% | $133,440,766.38 |
| JCT/USDT:USDT | +13.66% | $2,197,633.65 |
| STRAX/USDT:USDT | +6.94% | $1,207,273.61 |
| UAI/USDT:USDT | +5.45% | $2,195,894.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FOLKS/USDT:USDT | below_1h_threshold | +4.27% | +4.35% |
| STRAX/USDT:USDT | below_1h_threshold | +4.26% | +4.34% |
| JCT/USDT:USDT | below_1h_threshold | +3.78% | +3.87% |
| HMSTR/USDT:USDT | below_1h_threshold | +2.99% | +3.08% |
| BSB/USDT:USDT | below_1h_threshold | +2.30% | +2.38% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
