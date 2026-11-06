# Decision Report

- generated_at: 2026-11-06T00:16:17.136546+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18214**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.75% / filled 20/20。**
- 全期間 MARKET基準: n=18214, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=+1.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.90% | **+1.61%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.42% | **+1.07%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.80% | **+0.32%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.20% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.19% | **+0.06%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.10% | **-0.05%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 263件 (TP 96 / SL 159 / EXP 8)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,507.12** / 初期 $100.00 (+1407.12%)
- 確定: 7019件 (Win 2022 / Loss 2243 / Flat 2754) / skip 7756件
- 成長率目線: 平均log +0.000386 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APPSTOCK/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,507.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$375.26** / 初期 $100.00 (+275.26%)
- 確定: 4606件 (Win 1235 / Loss 1030 / Flat 2341) / skip 7019件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0575 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.08% 残高後 $375.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6376件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000450 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-06T00:16:06.555722+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=76171.6
- Funnel: target 1084 → liquid 189 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CYBER/USDT:USDT | +33.90% | $1,191,713.33 |
| CLANKER/USDT:USDT | +18.30% | $6,404,861.83 |
| BLESS/USDT:USDT | +14.06% | $5,328,765.03 |
| UVXY/USDT:USDT | +11.83% | $2,907,088.33 |
| BTW/USDT:USDT | +9.48% | $6,079,166.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ELSA/USDT:USDT | below_1h_threshold | +2.74% | +2.58% |
| WLFI/USDT:USDT | below_1h_threshold | +1.98% | +1.82% |
| RENDER/USDT:USDT | below_1h_threshold | +1.73% | +1.57% |
| BTW/USDT:USDT | below_1h_threshold | +1.71% | +1.55% |
| ICNT/USDT:USDT | below_1h_threshold | +1.63% | +1.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
