# Decision Report

- generated_at: 2026-05-11T14:23:01.046358+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4039**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4039, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-1.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.35% | **-1.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_3PCT | 18/20 | 90.0% | -0.05% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.81% | **+1.09%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.07% | **+1.07%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.33% | **+1.05%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.46% | **+1.04%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.68% | **+1.01%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 382件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T14:22:56.437361+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=80912.8
- Funnel: target 762 → liquid 184 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.6 >= 65=1, 4h RSI 85.2 >= 65=1, 4h RSI 72.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +51.94% | $4,619,034.91 |
| B/USDT:USDT | +41.98% | $14,583,447.72 |
| US/USDT:USDT | +38.73% | $14,697,257.40 |
| PENGUIN/USDT:USDT | +37.04% | $1,817,544.36 |
| SAGA/USDT:USDT | +30.94% | $3,829,323.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +4.32% | +4.47% |
| TRUTH/USDT:USDT | below_1h_threshold | +2.08% | +2.23% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +1.90% | +2.05% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.44% | +1.59% |
| BRETT/USDT:USDT | below_1h_threshold | +1.31% | +1.46% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
