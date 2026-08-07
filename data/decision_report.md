# Decision Report

- generated_at: 2026-08-07T11:36:33.217475+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10706**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10706, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.27% | **-1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.20% | **+0.72%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.76% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +3.46% | **+2.07%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.68% | **+1.74%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.73% | **+0.78%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.95% | **+0.76%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.19% | **+0.66%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3798件 (Win 1203 / Loss 1250 / Flat 1345) / skip 3469件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.49** / 初期 $100.00 (+44.49%)
- 確定: 1456件 (Win 407 / Loss 342 / Flat 707) / skip 2661件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0029 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $144.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.87** / 初期 $100.00 (+16.87%)
- 確定: 1161件 (Win 372 / Loss 456 / Flat 333) / pending 4件 / skip 1017件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000268 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $116.87

## 6. Latest Market Context

- 更新: 2026-08-07T11:36:20.959431+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=65004.9
- Funnel: target 961 → liquid 192 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KGEN/USDT:USDT | +41.32% | $1,160,808.62 |
| BICO/USDT:USDT | +36.12% | $27,660,407.98 |
| CATE/USDT:USDT | +33.73% | $4,341,817.82 |
| SKYAI/USDT:USDT | +29.24% | $72,711,660.78 |
| ON/USDT:USDT | +26.42% | $11,984,590.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ETHFI/USDT:USDT | below_1h_threshold | +2.76% | +2.55% |
| ALLO/USDT:USDT | below_1h_threshold | +2.42% | +2.20% |
| BSB/USDT:USDT | below_1h_threshold | +2.21% | +2.00% |
| ON/USDT:USDT | below_1h_threshold | +1.96% | +1.74% |
| BEAT/USDT:USDT | below_1h_threshold | +1.92% | +1.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
