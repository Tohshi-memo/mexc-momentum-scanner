# Decision Report

- generated_at: 2026-05-11T08:42:54.229644+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4020**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.02% / filled 20/20。**
- 全期間 MARKET基準: n=4020, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.02% | **+1.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.02% | **+1.02%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.22% | **+0.80%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_4PCT | 9/20 | 45.0% | +0.92% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 10/11 | 90.9% | +0.39% | **+0.36%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.04% | **-0.01%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.47% | **-0.16%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.43% | **-0.26%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.65% | **-0.29%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 363件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T08:42:50.868559+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=80783.0
- Funnel: target 760 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +39.34% | $11,703,353.45 |
| B/USDT:USDT | +24.91% | $8,002,464.14 |
| VVV/USDT:USDT | +17.80% | $13,247,639.75 |
| SAGA/USDT:USDT | +17.51% | $1,955,709.73 |
| ALCH/USDT:USDT | +17.14% | $4,624,529.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_relative_strength | +5.06% | +4.96% |
| UB/USDT:USDT | below_1h_threshold | +3.03% | +2.94% |
| TRUTH/USDT:USDT | below_1h_threshold | +2.25% | +2.15% |
| JELLYJELLY/USDT:USDT | below_1h_threshold | +1.93% | +1.84% |
| US/USDT:USDT | below_1h_threshold | +1.91% | +1.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
