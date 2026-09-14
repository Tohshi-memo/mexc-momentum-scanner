# Decision Report

- generated_at: 2026-09-14T07:16:23.671215+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14498**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14498, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.38% | **-1.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.94% | **+0.42%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.04% | **+0.04%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.04% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +5.83% | **+2.62%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +3.98% | **+2.58%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +3.43% | **+2.57%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +3.23% | **+2.26%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +3.50% | **+1.92%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,072.66** / 初期 $100.00 (+972.66%)
- 確定: 5434件 (Win 1635 / Loss 1762 / Flat 2037) / skip 5625件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PUNDIX/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.22% 残高後 $1,072.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$227.62** / 初期 $100.00 (+127.62%)
- 確定: 2991件 (Win 830 / Loss 716 / Flat 1445) / skip 4918件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0598 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $227.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$127.09** / 初期 $100.00 (+27.09%)
- 確定: 2879件 (Win 859 / Loss 1113 / Flat 907) / pending 6件 / skip 3087件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000294 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ARK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $127.09

## 6. Latest Market Context

- 更新: 2026-09-14T07:16:14.012139+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=77614.8
- Funnel: target 1068 → liquid 145 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.1 >= 65=1, 4h RSI 77.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +53.81% | $1,714,636.95 |
| AIN/USDT:USDT | +50.24% | $1,426,983.32 |
| BR/USDT:USDT | +33.90% | $4,882,818.97 |
| MTL/USDT:USDT | +31.45% | $1,461,821.98 |
| ARK/USDT:USDT | +30.10% | $4,569,044.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STEEM/USDT:USDT | below_1h_threshold | +4.22% | +4.14% |
| POWER/USDT:USDT | below_1h_threshold | +2.77% | +2.69% |
| POWR/USDT:USDT | below_1h_threshold | +2.37% | +2.29% |
| PUNDIX/USDT:USDT | below_1h_threshold | +2.23% | +2.16% |
| PONS/USDT:USDT | below_1h_threshold | +1.48% | +1.40% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
