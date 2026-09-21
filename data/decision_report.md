# Decision Report

- generated_at: 2026-09-21T21:16:22.239235+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15280**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15280, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.06% | **-1.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 15/20 | 75.0% | +0.86% | **+0.65%** |
| LIMIT_BB3S | 8/16 | 50.0% | +0.63% | **+0.32%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.88% | **+0.22%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.13% | **+0.03%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.08% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.04% | **+1.73%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.07% | **+1.45%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.92% | **+1.25%** |
| MARKET_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_8PCT_LONG | 3/20 | 15.0% | +2.67% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,192.71** / 初期 $100.00 (+1092.71%)
- 確定: 5771件 (Win 1717 / Loss 1853 / Flat 2201) / skip 6070件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARB/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $1,192.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$250.53** / 初期 $100.00 (+150.53%)
- 確定: 3321件 (Win 918 / Loss 766 / Flat 1637) / skip 5370件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0739 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PTB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $250.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.42** / 初期 $100.00 (+23.42%)
- 確定: 3053件 (Win 898 / Loss 1192 / Flat 963) / pending 5件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000313 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ARB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $123.42

## 6. Latest Market Context

- 更新: 2026-09-21T21:16:11.271191+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.42% price=86596.0
- Funnel: target 1055 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FORM/USDT:USDT | +28.79% | $7,966,295.29 |
| ALCH/USDT:USDT | +27.27% | $1,465,269.55 |
| SYN/USDT:USDT | +13.60% | $6,831,236.26 |
| EVAA/USDT:USDT | +12.32% | $1,665,503.92 |
| PTB/USDT:USDT | +11.57% | $1,186,591.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +1.53% | +1.95% |
| RUNE/USDT:USDT | below_1h_threshold | +1.08% | +1.50% |
| NEAR/USDT:USDT | below_1h_threshold | +0.93% | +1.35% |
| XMR/USDT:USDT | below_1h_threshold | +0.91% | +1.33% |
| ALLO/USDT:USDT | below_1h_threshold | +0.90% | +1.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
