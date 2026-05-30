# Decision Report

- generated_at: 2026-05-30T03:05:00.405692+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5095**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5095, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.48% | **-0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 5/20 | 25.0% | +7.32% | **+1.83%** |
| LIMIT_10PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_8PCT | 6/20 | 30.0% | +1.85% | **+0.56%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +0.51% | **+0.30%** |
| LIMIT_7PCT | 7/20 | 35.0% | -0.11% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.75% | **+1.75%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +4.53% | **+1.13%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_7PCT_LONG | 3/20 | 15.0% | +4.97% | **+0.75%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.27% | **+0.70%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 753件 (Win 175 / Loss 226 / Flat 352) / skip 903件
- 成長率目線: 平均log +0.000304 / 幾何平均 +0.030% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-30T03:04:57.606674+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=73729.6
- Funnel: target 773 → liquid 148 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +55.51% | $10,724,648.68 |
| XLM/USDT:USDT | +33.41% | $445,870,327.78 |
| LAB/USDT:USDT | +21.65% | $133,485,337.64 |
| OL/USDT:USDT | +19.06% | $1,532,034.97 |
| BASED/USDT:USDT | +17.76% | $2,535,752.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_1h_threshold | +1.54% | +1.56% |
| CLO/USDT:USDT | below_1h_threshold | +0.94% | +0.97% |
| LAB/USDT:USDT | below_1h_threshold | +0.91% | +0.94% |
| BEAT/USDT:USDT | below_1h_threshold | +0.76% | +0.78% |
| HBAR/USDT:USDT | below_1h_threshold | +0.75% | +0.78% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
