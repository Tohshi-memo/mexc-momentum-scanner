# Decision Report

- generated_at: 2026-05-25T07:59:25.147101+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4849**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4849, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.17% | **-0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +2.61% | **+0.39%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +3.34% | **+3.34%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.64% | **+1.39%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.62% | **+1.13%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.48% | **+1.03%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.10% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.50** / 初期 $100.00 (+26.50%)
- 確定: 655件 (Win 164 / Loss 206 / Flat 285) / skip 755件
- 成長率目線: 平均log +0.000359 / 幾何平均 +0.036% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $126.50

## 4. Latest Market Context

- 更新: 2026-05-25T07:59:18.059953+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=77350.3
- Funnel: target 764 → liquid 118 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XAN/USDT:USDT | +41.87% | $5,046,240.12 |
| PLAY/USDT:USDT | +37.61% | $4,981,615.68 |
| SAGA/USDT:USDT | +14.43% | $1,549,912.16 |
| SPORTFUN/USDT:USDT | +12.42% | $1,315,835.71 |
| H/USDT:USDT | +11.48% | $1,332,427.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +3.87% | +3.91% |
| SAGA/USDT:USDT | below_1h_threshold | +3.47% | +3.51% |
| PLUME/USDT:USDT | below_1h_threshold | +2.02% | +2.07% |
| XLM/USDT:USDT | below_1h_threshold | +1.29% | +1.34% |
| XAN/USDT:USDT | below_1h_threshold | +1.28% | +1.32% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
