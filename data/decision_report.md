# Decision Report

- generated_at: 2026-10-06T15:01:29.674968+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16222**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16222, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.42% | **-0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.53% | **+0.21%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.94% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.11% | **+1.11%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.53% | **+0.38%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +0.48% | **+0.29%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +0.74% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$120.39** / 初期 $100.00 (+20.39%)
- 確定トレード: 231件 (TP 83 / SL 141 / EXP 7)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.39
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,356.09** / 初期 $100.00 (+1256.09%)
- 確定: 6263件 (Win 1842 / Loss 2003 / Flat 2418) / skip 6520件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MRVLSTOCK/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $1,356.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.97** / 初期 $100.00 (+175.97%)
- 確定: 3630件 (Win 1010 / Loss 851 / Flat 1769) / skip 6003件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0129 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MRVLSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $275.97

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4385件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000361 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-06T15:01:18.111388+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=86622.1
- Funnel: target 1074 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZCAT/USDT:USDT | +65.18% | $1,008,903.59 |
| RLC/USDT:USDT | +58.75% | $41,294,725.04 |
| BR/USDT:USDT | +46.28% | $57,124,581.10 |
| US/USDT:USDT | +39.08% | $1,395,403.02 |
| ORCA/USDT:USDT | +37.18% | $3,847,839.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +1.75% | +1.69% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +1.75% | +1.69% |
| AVGOSTOCK/USDT:USDT | below_1h_threshold | +1.58% | +1.51% |
| ORCA/USDT:USDT | below_1h_threshold | +0.86% | +0.79% |
| ORDI/USDT:USDT | below_1h_threshold | +0.53% | +0.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
