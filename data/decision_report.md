# Decision Report

- generated_at: 2026-06-10T08:12:15.516643+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6200**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6200, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.55% | **-1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.37% | **+0.17%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.50% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.55% | **+1.55%** |
| ASK_LONG | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +4.00% | **+0.80%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.72% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$152.79** / 初期 $100.00 (+52.79%)
- 確定: 1216件 (Win 303 / Loss 376 / Flat 537) / skip 1545件
- 成長率目線: 平均log +0.000349 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $152.79

## 4. Latest Market Context

- 更新: 2026-06-10T08:12:12.146408+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=61676.3
- Funnel: target 781 → liquid 148 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +49.80% | $8,160,409.70 |
| ESPORTS/USDT:USDT | +49.59% | $23,283,697.74 |
| BTW/USDT:USDT | +27.66% | $29,954,728.30 |
| UB/USDT:USDT | +18.15% | $2,083,876.18 |
| BLESS/USDT:USDT | +13.65% | $3,562,821.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TXNSTOCK/USDT:USDT | below_1h_threshold | +3.10% | +3.07% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.58% | +2.54% |
| OPN/USDT:USDT | below_1h_threshold | +1.97% | +1.93% |
| BABY/USDT:USDT | below_1h_threshold | +1.42% | +1.38% |
| BEAT/USDT:USDT | below_1h_threshold | +1.36% | +1.33% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
