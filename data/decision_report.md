# Decision Report

- generated_at: 2026-07-13T18:46:13.612261+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8649**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8649, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.76% | **+0.97%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.66% | **+0.83%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +1.01% | **+0.20%** |
| LIMIT_BB3S | 5/20 | 25.0% | -0.74% | **-0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.78% | **+2.08%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +2.80% | **+1.68%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.34% | **+1.52%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.61% | **+1.44%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.19% | **+1.07%** |

## 2. $100 Live Portfolio

- 残高: **$101.19** / 初期 $100.00 (+1.19%)
- 確定トレード: 94件 (TP 31 / SL 61 / EXP 2)
- 最新: AIOT/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$328.48** / 初期 $100.00 (+228.48%)
- 確定: 2817件 (Win 886 / Loss 923 / Flat 1008) / skip 2393件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $328.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.26** / 初期 $100.00 (+5.26%)
- 確定: 650件 (Win 154 / Loss 159 / Flat 337) / skip 1410件
- 成長率目線: 平均log +0.000079 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0149 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.48** / 初期 $100.00 (-0.52%)
- 確定: 39件 (Win 14 / Loss 25 / Flat 0) / pending 0件 / skip 78件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000368 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $99.48

## 6. Latest Market Context

- 更新: 2026-07-13T18:46:07.285954+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=61979.9
- Funnel: target 867 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIOT/USDT:USDT | +25.04% | $2,919,661.65 |
| ALLO/USDT:USDT | +15.93% | $27,741,545.99 |
| VELVET/USDT:USDT | +6.16% | $28,844,713.43 |
| EVAA/USDT:USDT | +5.14% | $21,195,248.20 |
| BEAT/USDT:USDT | +4.77% | $16,970,423.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +4.89% | +4.73% |
| BEAT/USDT:USDT | below_1h_threshold | +4.49% | +4.33% |
| AIOT/USDT:USDT | below_1h_threshold | +4.20% | +4.04% |
| DEXE/USDT:USDT | below_1h_threshold | +3.55% | +3.39% |
| DODO/USDT:USDT | below_1h_threshold | +3.13% | +2.97% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
