# Decision Report

- generated_at: 2026-10-26T06:06:20.195511+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17465**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.60% / filled 20/20。**
- 全期間 MARKET基準: n=17465, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.83% | **+1.55%** |
| LIMIT_ATR | 6/20 | 30.0% | +4.78% | **+1.43%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +4.21% | **+0.84%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +0.37% | **+0.13%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.13% | **+0.03%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | -0.42% | **-0.38%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | -0.57% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 251件 (TP 93 / SL 150 / EXP 8)
- 最新: CT/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,542.31** / 初期 $100.00 (+1442.31%)
- 確定: 6718件 (Win 1956 / Loss 2150 / Flat 2612) / skip 7308件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RLS/USDT:USDT `LIMIT_7PCT_LONG` SL_HIT account -0.50% 残高後 $1,542.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$314.85** / 初期 $100.00 (+214.85%)
- 確定: 4008件 (Win 1111 / Loss 949 / Flat 1948) / skip 6868件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0371 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RLS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $314.85

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5623件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000185 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-26T06:06:05.688974+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=80147.5
- Funnel: target 1070 → liquid 139 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KIMCHI/USDT:USDT | +49.53% | $2,973,322.66 |
| DODO/USDT:USDT | +10.32% | $1,186,009.96 |
| BR/USDT:USDT | +9.96% | $8,556,918.79 |
| RLS/USDT:USDT | +8.53% | $1,050,308.71 |
| CLAUDIA/USDT:USDT | +8.42% | $1,116,050.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNITREE/USDT:USDT | below_1h_threshold | +3.93% | +4.04% |
| KIMCHI/USDT:USDT | below_1h_threshold | +1.88% | +1.99% |
| NIL/USDT:USDT | below_1h_threshold | +0.90% | +1.00% |
| SOXS/USDT:USDT | below_1h_threshold | +0.69% | +0.80% |
| TESLA/USDT:USDT | below_1h_threshold | +0.32% | +0.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
