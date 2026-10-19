# Decision Report

- generated_at: 2026-10-19T07:21:18.871212+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16999**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16999, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.64% | **+0.49%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.28% | **+0.22%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.05% | **+0.90%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.15% | **+0.81%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.04% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,270.02** / 初期 $100.00 (+1170.02%)
- 確定: 6444件 (Win 1871 / Loss 2059 / Flat 2514) / skip 7116件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,270.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.58** / 初期 $100.00 (+178.58%)
- 確定: 3764件 (Win 1038 / Loss 882 / Flat 1844) / skip 6646件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0389 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $278.58

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5159件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000113 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-19T07:21:07.034422+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=82792.4
- Funnel: target 1085 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +25.34% | $8,486,384.76 |
| ZEREBRO/USDT:USDT | +23.12% | $1,744,485.74 |
| KORU/USDT:USDT | +19.58% | $64,740,169.89 |
| BR/USDT:USDT | +18.93% | $14,732,708.23 |
| UNITREE/USDT:USDT | +17.66% | $1,665,272.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNITREE/USDT:USDT | below_1h_threshold | +4.34% | +4.37% |
| BR/USDT:USDT | below_1h_threshold | +3.74% | +3.76% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.29% | +1.32% |
| WLD/USDT:USDT | below_1h_threshold | +0.79% | +0.81% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.76% | +0.79% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
