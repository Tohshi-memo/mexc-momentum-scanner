# Decision Report

- generated_at: 2026-10-19T14:01:17.756771+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17012**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.92% / filled 20/20。**
- 全期間 MARKET基準: n=17012, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.92% | **+2.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.92% | **+2.92%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.80% | **+2.38%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.18% | **+1.53%** |
| LIMIT_3PCT | 10/20 | 50.0% | +0.75% | **+0.38%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.71% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +3.04% | **+0.91%** |
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +1.33% | **+0.80%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +1.55% | **+0.62%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.33% | **-0.20%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | -0.78% | **-0.47%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,257.25** / 初期 $100.00 (+1157.25%)
- 確定: 6457件 (Win 1872 / Loss 2063 / Flat 2522) / skip 7116件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ICNT/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $1,257.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.61** / 初期 $100.00 (+177.61%)
- 確定: 3777件 (Win 1038 / Loss 883 / Flat 1856) / skip 6646件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0296 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ICNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $277.61

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5172件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000095 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-19T14:01:05.581200+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=82055.8
- Funnel: target 1090 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +24.11% | $10,515,027.68 |
| SNXX/USDT:USDT | +19.58% | $33,101,331.54 |
| KORU/USDT:USDT | +19.09% | $99,287,133.24 |
| ZEREBRO/USDT:USDT | +17.80% | $1,910,707.77 |
| UNITREE/USDT:USDT | +14.97% | $2,222,184.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +4.45% | +4.49% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +3.03% | +3.08% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.39% | +2.43% |
| TESLA/USDT:USDT | below_1h_threshold | +1.87% | +1.91% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +0.93% | +0.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
