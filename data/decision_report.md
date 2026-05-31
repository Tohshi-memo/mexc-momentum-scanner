# Decision Report

- generated_at: 2026-05-31T20:37:11.777851+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5224**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5224, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.92% | **-1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +2.65% | **+1.06%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.59% | **+0.88%** |
| LIMIT_BB3S | 11/19 | 57.9% | +0.39% | **+0.23%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.54% | **+1.77%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.98% | **+1.49%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.46% | **+1.17%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.03% | **+1.12%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.78% | **+1.11%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.16** / 初期 $100.00 (+31.16%)
- 確定: 859件 (Win 199 / Loss 255 / Flat 405) / skip 926件
- 成長率目線: 平均log +0.000316 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BIANRENSHENG/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $131.16

## 4. Latest Market Context

- 更新: 2026-05-31T20:37:09.365434+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=73667.0
- Funnel: target 773 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +35.92% | $15,653,968.87 |
| PORTAL/USDT:USDT | +14.87% | $11,745,473.52 |
| BIANRENSHENG/USDT:USDT | +13.61% | $3,143,863.64 |
| ZORA/USDT:USDT | +11.78% | $1,418,920.10 |
| HOME/USDT:USDT | +9.22% | $2,648,702.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FET/USDT:USDT | below_1h_threshold | +2.31% | +2.12% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +2.27% | +2.08% |
| GRASS/USDT:USDT | below_1h_threshold | +1.97% | +1.77% |
| DYDX/USDT:USDT | below_1h_threshold | +1.74% | +1.55% |
| XLM/USDT:USDT | below_1h_threshold | +1.61% | +1.42% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
