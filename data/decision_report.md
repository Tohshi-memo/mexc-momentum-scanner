# Decision Report

- generated_at: 2026-06-12T07:28:28.064426+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6479**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6479, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/20 | 15.0% | +3.20% | **+0.48%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.03% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +3.00% | **+3.00%** |
| ASK_LONG | 20/20 | 100.0% | +2.92% | **+2.92%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +3.32% | **+2.33%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +3.53% | **+1.94%** |
| LIMIT_ATR_LONG | 6/20 | 30.0% | +4.92% | **+1.48%** |

## 2. $100 Live Portfolio

- 残高: **$95.17** / 初期 $100.00 (-4.83%)
- 確定トレード: 17件 (TP 2 / SL 14 / EXP 1)
- 最新: ZBT/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$165.61** / 初期 $100.00 (+65.61%)
- 確定: 1354件 (Win 366 / Loss 432 / Flat 556) / skip 1686件
- 成長率目線: 平均log +0.000373 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NAORIS/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $165.61

## 4. Latest Market Context

- 更新: 2026-06-12T07:28:21.882139+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=62999.1
- Funnel: target 779 → liquid 156 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +101.65% | $139,965,866.29 |
| ESPORTS/USDT:USDT | +47.80% | $34,500,973.09 |
| H/USDT:USDT | +38.85% | $44,320,335.07 |
| NAORIS/USDT:USDT | +37.42% | $2,200,389.63 |
| XPL/USDT:USDT | +30.20% | $7,384,886.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HMSTR/USDT:USDT | below_1h_threshold | +4.27% | +4.20% |
| LAB/USDT:USDT | below_1h_threshold | +3.80% | +3.73% |
| NAORIS/USDT:USDT | below_1h_threshold | +3.25% | +3.18% |
| NEAR/USDT:USDT | below_1h_threshold | +2.98% | +2.91% |
| UB/USDT:USDT | below_1h_threshold | +2.45% | +2.39% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
