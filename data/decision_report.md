# Decision Report

- generated_at: 2026-06-11T14:27:35.039638+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6357**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6357, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.24% | **+0.22%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.02% | **+0.02%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.01% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.12% | **+1.12%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.83% | **+0.62%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.64% | **+0.32%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.66** / 初期 $100.00 (+49.66%)
- 確定: 1277件 (Win 323 / Loss 403 / Flat 551) / skip 1641件
- 成長率目線: 平均log +0.000316 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPACE/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $149.66

## 4. Latest Market Context

- 更新: 2026-06-11T14:27:27.269514+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=62869.9
- Funnel: target 782 → liquid 154 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +110.37% | $25,385,497.02 |
| VELVET/USDT:USDT | +89.76% | $85,021,988.74 |
| BEAT/USDT:USDT | +62.97% | $243,460,977.84 |
| AIO/USDT:USDT | +54.44% | $8,886,011.08 |
| COLLECT/USDT:USDT | +52.24% | $2,362,745.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +3.33% | +3.59% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.64% | +1.90% |
| ASTR/USDT:USDT | below_1h_threshold | +1.43% | +1.69% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.23% | +1.50% |
| STG/USDT:USDT | below_1h_threshold | +1.21% | +1.47% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
