# Decision Report

- generated_at: 2026-09-10T01:41:14.846504+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14139**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.16% / filled 20/20。**
- 全期間 MARKET基準: n=14139, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.27% | **+1.14%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.24% | **+1.12%** |
| LIMIT_6PCT | 4/20 | 20.0% | +4.94% | **+0.99%** |
| LIMIT_5PCT | 7/20 | 35.0% | +2.26% | **+0.79%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +2.31% | **+1.96%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +1.54% | **+1.46%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.52% | **+0.28%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.28% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,019.55** / 初期 $100.00 (+919.55%)
- 確定: 5319件 (Win 1598 / Loss 1717 / Flat 2004) / skip 5381件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,019.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$202.19** / 初期 $100.00 (+102.19%)
- 確定: 2733件 (Win 754 / Loss 641 / Flat 1338) / skip 4817件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0680 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $202.19

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.58** / 初期 $100.00 (+20.58%)
- 確定: 2644件 (Win 778 / Loss 1011 / Flat 855) / pending 4件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000455 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $120.58

## 6. Latest Market Context

- 更新: 2026-09-10T01:41:05.166624+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=77991.9
- Funnel: target 1064 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VTHO/USDT:USDT | +41.82% | $1,055,289.61 |
| CATE/USDT:USDT | +17.02% | $2,848,469.60 |
| BTR/USDT:USDT | +12.80% | $2,254,451.34 |
| SOCK/USDT:USDT | +5.85% | $1,102,414.77 |
| WAVES/USDT:USDT | +4.58% | $1,112,974.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VTHO/USDT:USDT | below_1h_threshold | +4.41% | +4.60% |
| SOXS/USDT:USDT | below_1h_threshold | +1.48% | +1.66% |
| BR/USDT:USDT | below_1h_threshold | +1.10% | +1.29% |
| AKE/USDT:USDT | below_1h_threshold | +1.06% | +1.24% |
| ANTHROPIC/USDT:USDT | below_1h_threshold | +0.67% | +0.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
