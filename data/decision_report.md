# Decision Report

- generated_at: 2026-07-06T14:40:45.926758+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8395**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8395, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.24% | **-1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +2.16% | **+0.54%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.44% | **+0.49%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_BB3S | 8/12 | 66.7% | +0.53% | **+0.35%** |
| LIMIT_10PCT | 3/20 | 15.0% | +2.30% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.92% | **+1.75%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.93% | **+1.25%** |
| ASK_LONG | 20/20 | 100.0% | +1.24% | **+1.24%** |
| MARKET_LONG | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_BB3S_LONG | 4/8 | 50.0% | +2.08% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$101.57** / 初期 $100.00 (+1.57%)
- 確定トレード: 67件 (TP 23 / SL 43 / EXP 1)
- 最新: EPIC/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.57
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$317.13** / 初期 $100.00 (+217.13%)
- 確定: 2623件 (Win 832 / Loss 887 / Flat 904) / skip 2333件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VANRY/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $317.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 639件 (Win 152 / Loss 158 / Flat 329) / skip 1167件
- 成長率目線: 平均log +0.000084 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASED/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.26% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-06T14:40:40.916526+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.58% price=62105.0
- Funnel: target 841 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VANRY/USDT:USDT | +74.60% | $11,898,592.92 |
| YFI/USDT:USDT | +21.19% | $4,684,986.56 |
| TRIA/USDT:USDT | +19.56% | $2,914,185.29 |
| SCRT/USDT:USDT | +16.71% | $1,036,707.59 |
| DEXE/USDT:USDT | +16.60% | $2,181,250.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TLM/USDT:USDT | below_relative_strength | +5.33% | +4.75% |
| LIT/USDT:USDT | below_1h_threshold | +3.94% | +3.36% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.82% | +2.24% |
| ORDI/USDT:USDT | below_1h_threshold | +2.49% | +1.91% |
| BEL/USDT:USDT | below_1h_threshold | +2.45% | +1.87% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
