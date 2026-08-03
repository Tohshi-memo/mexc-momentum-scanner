# Decision Report

- generated_at: 2026-08-03T16:01:27.987577+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10232**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10232, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_8PCT | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.39% | **+2.39%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.51% | **+2.26%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.20% | **+1.92%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.61% | **+1.17%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +1.32% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$585.39** / 初期 $100.00 (+485.39%)
- 確定: 3691件 (Win 1171 / Loss 1207 / Flat 1313) / skip 3102件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $585.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1283件 (Win 359 / Loss 298 / Flat 626) / skip 2360件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0203 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.28** / 初期 $100.00 (+16.28%)
- 確定: 1015件 (Win 327 / Loss 393 / Flat 295) / pending 4件 / skip 685件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000503 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $116.28

## 6. Latest Market Context

- 更新: 2026-08-03T16:01:19.270893+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=63638.9
- Funnel: target 929 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GRVT/USDT:USDT | +1.07% | $2,423,873.17 |
| COTI/USDT:USDT | +0.72% | $1,613,975.18 |
| SOXL/USDT:USDT | +0.70% | $77,235,653.51 |
| ESPORTS/USDT:USDT | +0.57% | $1,318,443.86 |
| KORU/USDT:USDT | +0.53% | $11,351,167.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRVT/USDT:USDT | below_1h_threshold | +0.90% | +0.93% |
| COTI/USDT:USDT | below_1h_threshold | +0.72% | +0.76% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +0.67% | +0.70% |
| ESPORTS/USDT:USDT | below_1h_threshold | +0.57% | +0.60% |
| TAKE/USDT:USDT | below_1h_threshold | +0.56% | +0.59% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
