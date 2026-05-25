# Decision Report

- generated_at: 2026-05-25T08:09:06.184010+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4851**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4851, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.75% | **-0.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.19% | **+0.44%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.40% | **+0.36%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +3.34% | **+3.34%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.99% | **+1.59%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.05% | **+1.33%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.90% | **+1.23%** |
| MARKET_LONG | 20/20 | 100.0% | +0.93% | **+0.93%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.50** / 初期 $100.00 (+26.50%)
- 確定: 657件 (Win 164 / Loss 206 / Flat 287) / skip 755件
- 成長率目線: 平均log +0.000358 / 幾何平均 +0.036% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $126.50

## 4. Latest Market Context

- 更新: 2026-05-25T08:09:04.033330+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=77323.3
- Funnel: target 764 → liquid 117 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +40.40% | $5,238,939.90 |
| XAN/USDT:USDT | +39.71% | $5,253,905.67 |
| SAGA/USDT:USDT | +14.54% | $1,537,560.18 |
| PHA/USDT:USDT | +11.89% | $1,226,550.44 |
| UB/USDT:USDT | +11.84% | $5,844,009.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PHA/USDT:USDT | below_1h_threshold | +4.33% | +4.40% |
| BILL/USDT:USDT | below_1h_threshold | +2.31% | +2.38% |
| PLAY/USDT:USDT | below_1h_threshold | +2.08% | +2.15% |
| UB/USDT:USDT | below_1h_threshold | +1.47% | +1.54% |
| NIL/USDT:USDT | below_1h_threshold | +1.07% | +1.14% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
