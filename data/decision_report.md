# Decision Report

- generated_at: 2026-05-21T01:39:12.016239+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4589**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4589, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_6PCT | 8/20 | 40.0% | +0.47% | **+0.19%** |
| LIMIT_7PCT | 7/20 | 35.0% | +0.40% | **+0.14%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_8PCT | 6/20 | 30.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +3.77% | **+2.45%** |
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +2.49% | **+2.14%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.95% | **+1.77%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +3.08% | **+1.39%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.17% | **+1.08%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 545件 (Win 138 / Loss 185 / Flat 222) / skip 605件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T01:39:07.213182+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=77800.0
- Funnel: target 763 → liquid 129 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +64.76% | $1,085,459.38 |
| EDEN/USDT:USDT | +41.29% | $28,432,237.61 |
| BSB/USDT:USDT | +33.07% | $59,175,615.79 |
| NIL/USDT:USDT | +20.37% | $3,336,947.50 |
| FIDA/USDT:USDT | +16.91% | $11,983,687.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JTO/USDT:USDT | below_1h_threshold | +2.59% | +2.75% |
| ONDO/USDT:USDT | below_1h_threshold | +2.49% | +2.66% |
| FIDA/USDT:USDT | below_1h_threshold | +2.15% | +2.32% |
| FIGHT/USDT:USDT | below_1h_threshold | +1.98% | +2.15% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +1.59% | +1.76% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
