# Decision Report

- generated_at: 2026-08-05T03:56:30.806646+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10347**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10347, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.85% | **-2.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.72% | **+0.52%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.83% | **+2.13%** |
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.06% | **+1.84%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +3.08% | **+1.39%** |
| LIMIT_4PCT_LONG | 6/20 | 30.0% | +4.20% | **+1.26%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$598.47** / 初期 $100.00 (+498.47%)
- 確定: 3744件 (Win 1186 / Loss 1224 / Flat 1334) / skip 3164件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HFT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $598.47

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1285件 (Win 359 / Loss 299 / Flat 627) / skip 2473件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0388 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.71** / 初期 $100.00 (+18.71%)
- 確定: 1103件 (Win 356 / Loss 425 / Flat 322) / pending 6件 / skip 716件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000318 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HFT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $118.71

## 6. Latest Market Context

- 更新: 2026-08-05T03:56:18.040364+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.32% price=64132.3
- Funnel: target 939 → liquid 183 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.4 >= 65=1, 4h RSI 70.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +83.40% | $8,855,573.54 |
| TAKE/USDT:USDT | +37.26% | $1,561,835.81 |
| CASHCAT/USDT:USDT | +31.82% | $1,187,158.48 |
| MARSCOIN/USDT:USDT | +29.86% | $1,149,307.87 |
| BLESS/USDT:USDT | +29.69% | $23,034,393.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAKE/USDT:USDT | below_1h_threshold | +3.64% | +3.96% |
| SYN/USDT:USDT | below_1h_threshold | +3.47% | +3.79% |
| CAP/USDT:USDT | below_1h_threshold | +1.60% | +1.93% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.32% | +1.65% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +1.29% | +1.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
