# Decision Report

- generated_at: 2026-05-09T03:27:48.519169+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3850**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3850, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-2.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.06% | **-2.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.42% | **+0.36%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.55% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +6.25% | **+2.19%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.55% | **+1.65%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.93% | **+1.46%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.51% | **+1.25%** |
| LIMIT_7PCT_LONG | 4/20 | 20.0% | +5.73% | **+1.15%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 193件 (Win 48 / Loss 64 / Flat 81) / skip 218件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T03:27:41.798270+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=80363.1
- Funnel: target 767 → liquid 176 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COLLECT/USDT:USDT | +28.52% | $7,115,725.06 |
| SATO/USDT:USDT | +24.58% | $4,159,816.09 |
| ICP/USDT:USDT | +22.67% | $232,590,224.40 |
| DEEP/USDT:USDT | +18.84% | $1,698,135.10 |
| CORE/USDT:USDT | +18.01% | $1,903,047.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_1h_threshold | +4.59% | +4.60% |
| CORE/USDT:USDT | below_1h_threshold | +2.38% | +2.39% |
| WIF/USDT:USDT | below_1h_threshold | +2.09% | +2.10% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.03% | +2.04% |
| BRETT/USDT:USDT | below_1h_threshold | +2.02% | +2.04% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
