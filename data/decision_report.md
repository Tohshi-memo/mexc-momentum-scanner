# Decision Report

- generated_at: 2026-09-04T01:21:26.154666+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13566**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.75% / filled 20/20。**
- 全期間 MARKET基準: n=13566, expectancy=-0.00%
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
| LIMIT_1PCT | 18/20 | 90.0% | +1.28% | **+1.15%** |
| LIMIT_BB3S | 4/19 | 21.1% | +4.67% | **+0.98%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.66% | **+0.40%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.22% | **+0.44%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.37% | **-0.33%** |
| MARKET_LONG | 20/20 | 100.0% | -0.35% | **-0.35%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5008件 (Win 1516 / Loss 1644 / Flat 1848) / skip 5119件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.36% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.25** / 初期 $100.00 (+85.25%)
- 確定: 2383件 (Win 676 / Loss 576 / Flat 1131) / skip 4594件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0554 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $185.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.02** / 初期 $100.00 (+17.02%)
- 確定: 2223件 (Win 663 / Loss 871 / Flat 689) / pending 3件 / skip 2811件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000271 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.05% 残高後 $117.02

## 6. Latest Market Context

- 更新: 2026-09-04T01:21:15.713489+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=80913.5
- Funnel: target 1046 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +29.08% | $9,499,501.73 |
| BASECAT/USDT:USDT | +20.85% | $1,848,671.51 |
| PONS/USDT:USDT | +16.87% | $9,328,141.84 |
| BTR/USDT:USDT | +12.13% | $9,057,817.83 |
| AKE/USDT:USDT | +11.73% | $25,358,922.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASECAT/USDT:USDT | below_1h_threshold | +4.99% | +5.02% |
| PONS/USDT:USDT | below_1h_threshold | +4.19% | +4.22% |
| BTR/USDT:USDT | below_1h_threshold | +4.12% | +4.15% |
| BR/USDT:USDT | below_1h_threshold | +3.65% | +3.68% |
| ZEST/USDT:USDT | below_1h_threshold | +1.52% | +1.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
