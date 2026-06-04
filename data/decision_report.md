# Decision Report

- generated_at: 2026-06-04T20:23:35.428158+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5664**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5664, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.65% | **-2.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +4.56% | **+1.14%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.62% | **+0.22%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.85% | **+2.85%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +4.06% | **+2.44%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.96% | **+2.37%** |
| ASK_LONG | 20/20 | 100.0% | +1.64% | **+1.64%** |
| LIMIT_3PCT_LONG | 6/20 | 30.0% | +3.74% | **+1.12%** |

## 2. $100 Live Portfolio

- 残高: **$98.05** / 初期 $100.00 (-1.95%)
- 確定トレード: 99件 (TP 30 / SL 66 / EXP 3)
- 最新: MONAD/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.05
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1007件 (Win 239 / Loss 312 / Flat 456) / skip 1218件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T20:23:32.751243+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.49% price=63288.5
- Funnel: target 771 → liquid 170 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +36.53% | $5,388,478.36 |
| OPN/USDT:USDT | +15.14% | $35,574,999.07 |
| HOME/USDT:USDT | +11.77% | $5,117,835.43 |
| AAOISTOCK/USDT:USDT | +11.45% | $1,021,334.77 |
| BIANRENSHENG/USDT:USDT | +7.41% | $1,609,999.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +4.27% | +4.76% |
| OPN/USDT:USDT | below_1h_threshold | +2.69% | +3.18% |
| BSB/USDT:USDT | below_1h_threshold | +2.25% | +2.74% |
| HEI/USDT:USDT | below_1h_threshold | +1.75% | +2.24% |
| XMR/USDT:USDT | below_1h_threshold | +0.80% | +1.29% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
