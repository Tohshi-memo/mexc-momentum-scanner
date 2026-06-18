# Decision Report

- generated_at: 2026-06-18T01:40:19.336098+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6990**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6990, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.45% | **+0.18%** |
| LIMIT_10PCT | 6/20 | 30.0% | -0.85% | **-0.25%** |
| LIMIT_ATR | 12/20 | 60.0% | -0.65% | **-0.39%** |
| LIMIT_8PCT | 7/20 | 35.0% | -1.19% | **-0.41%** |
| LIMIT_5PCT | 10/20 | 50.0% | -1.31% | **-0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +3.44% | **+3.44%** |
| MARKET_LONG | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.22% | **+1.33%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.80% | **+1.26%** |
| LIMIT_BB3S_LONG | 2/7 | 28.6% | +2.00% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$207.78** / 初期 $100.00 (+107.78%)
- 確定: 1836件 (Win 506 / Loss 579 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $207.78

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.07** / 初期 $100.00 (+5.07%)
- 確定: 263件 (Win 72 / Loss 67 / Flat 124) / skip 138件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0938 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BSB/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $105.07

## 5. Latest Market Context

- 更新: 2026-06-18T01:40:14.004438+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=64592.7
- Funnel: target 790 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +155.41% | $27,844,577.74 |
| O/USDT:USDT | +72.12% | $1,527,935.49 |
| SYN/USDT:USDT | +42.83% | $4,385,322.75 |
| H/USDT:USDT | +20.51% | $39,370,240.69 |
| MITO/USDT:USDT | +13.94% | $1,721,032.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XLM/USDT:USDT | below_relative_strength | +5.05% | +4.80% |
| FOLKS/USDT:USDT | below_1h_threshold | +4.61% | +4.36% |
| BEAT/USDT:USDT | below_1h_threshold | +3.09% | +2.84% |
| SIREN/USDT:USDT | below_1h_threshold | +2.81% | +2.56% |
| SYN/USDT:USDT | below_1h_threshold | +2.66% | +2.41% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
