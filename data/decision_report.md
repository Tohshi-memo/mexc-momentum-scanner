# Decision Report

- generated_at: 2026-09-09T04:01:16.766303+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14030**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.43% / filled 20/20。**
- 全期間 MARKET基準: n=14030, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.43% | **+2.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.43% | **+2.43%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.14% | **+1.93%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.44% | **+1.83%** |
| LIMIT_3PCT | 13/20 | 65.0% | +2.77% | **+1.80%** |
| LIMIT_ATR | 12/20 | 60.0% | +2.69% | **+1.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.40% | **+0.20%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | -0.46% | **-0.30%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -2.80% | **-0.56%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,008.51** / 初期 $100.00 (+908.51%)
- 確定: 5294件 (Win 1588 / Loss 1708 / Flat 1998) / skip 5297件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IOST/USDT:USDT `LIMIT_9PCT_LONG` SL_HIT account -0.50% 残高後 $1,008.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.99** / 初期 $100.00 (+89.99%)
- 確定: 2633件 (Win 726 / Loss 623 / Flat 1284) / skip 4808件
- 成長率目線: 平均log +0.000244 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0399 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IOST/USDT:USDT `LIMIT_9PCT_LONG` SL_HIT account -0.35% 残高後 $189.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.27** / 初期 $100.00 (+19.27%)
- 確定: 2611件 (Win 764 / Loss 993 / Flat 854) / pending 2件 / skip 2887件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000330 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: IOST/USDT:USDT `LIMIT_9PCT_LONG` SL_HIT account -0.17% 残高後 $119.27

## 6. Latest Market Context

- 更新: 2026-09-09T04:01:06.594410+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=78701.3
- Funnel: target 1070 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OL/USDT:USDT | +21.67% | $2,010,463.51 |
| WAVES/USDT:USDT | +12.18% | $1,513,850.76 |
| ARX/USDT:USDT | +10.59% | $1,460,078.48 |
| CNPY/USDT:USDT | +10.54% | $1,028,019.67 |
| NIULAI/USDT:USDT | +8.29% | $1,184,351.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XAN/USDT:USDT | below_1h_threshold | +0.98% | +0.84% |
| SOXS/USDT:USDT | below_1h_threshold | +0.95% | +0.81% |
| STRK/USDT:USDT | below_1h_threshold | +0.56% | +0.42% |
| UAI/USDT:USDT | below_1h_threshold | +0.49% | +0.36% |
| VVV/USDT:USDT | below_1h_threshold | +0.45% | +0.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
