# Decision Report

- generated_at: 2026-05-20T01:53:47.449515+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4517**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4517, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.06% | **-0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +2.71% | **+1.09%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.22% | **+0.55%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.07% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.86% | **+1.21%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.50% | **+0.90%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.72% | **+0.82%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.54** / 初期 $100.00 (+24.54%)
- 確定: 479件 (Win 127 / Loss 165 / Flat 187) / skip 599件
- 成長率目線: 平均log +0.000458 / 幾何平均 +0.046% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RLS/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $124.54

## 4. Latest Market Context

- 更新: 2026-05-20T01:53:42.530535+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=76759.5
- Funnel: target 764 → liquid 141 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROMPT/USDT:USDT | +38.68% | $12,660,388.44 |
| EDEN/USDT:USDT | +23.55% | $17,558,590.18 |
| LIT/USDT:USDT | +19.41% | $4,999,884.43 |
| BANANAS31/USDT:USDT | +17.73% | $1,591,554.49 |
| ZEST/USDT:USDT | +14.55% | $1,715,704.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +3.64% | +3.64% |
| PLAY/USDT:USDT | below_1h_threshold | +2.76% | +2.76% |
| FIGHT/USDT:USDT | below_1h_threshold | +2.55% | +2.56% |
| SPACE/USDT:USDT | below_1h_threshold | +2.37% | +2.37% |
| RIVER/USDT:USDT | below_1h_threshold | +2.21% | +2.21% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
