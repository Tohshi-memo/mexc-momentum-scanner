# Decision Report

- generated_at: 2026-05-21T07:23:46.021591+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4613**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.06% / filled 20/20。**
- 全期間 MARKET基準: n=4613, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+2.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |
| ASK | 20/20 | 100.0% | +1.65% | **+1.65%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.83% | **+1.37%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.35% | **+1.02%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.92% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.23% | **+1.00%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.64% | **+0.74%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.05% | **+0.47%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.04% | **-0.02%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | -0.05% | **-0.03%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 58件 (TP 15 / SL 40 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 545件 (Win 138 / Loss 185 / Flat 222) / skip 629件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T07:23:43.689764+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=77507.7
- Funnel: target 765 → liquid 132 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +39.80% | $1,956,037.77 |
| EDEN/USDT:USDT | +34.16% | $30,110,611.04 |
| SATO/USDT:USDT | +21.76% | $3,520,645.14 |
| USELESS/USDT:USDT | +17.14% | $1,518,802.33 |
| BEAT/USDT:USDT | +14.36% | $2,581,543.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +2.32% | +2.43% |
| BEAT/USDT:USDT | below_1h_threshold | +1.94% | +2.05% |
| HYPE/USDT:USDT | below_1h_threshold | +1.66% | +1.77% |
| LIT/USDT:USDT | below_1h_threshold | +1.22% | +1.33% |
| LAB/USDT:USDT | below_1h_threshold | +0.91% | +1.02% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
