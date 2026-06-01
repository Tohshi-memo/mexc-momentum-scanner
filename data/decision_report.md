# Decision Report

- generated_at: 2026-06-01T00:45:42.397985+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5245**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5245, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.41% | **-0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.60% | **+1.08%** |
| LIMIT_10PCT | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_9PCT | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_8PCT | 6/20 | 30.0% | -0.00% | **-0.00%** |
| ASK | 20/20 | 100.0% | -0.14% | **-0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/11 | 54.5% | +3.53% | **+1.93%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.81% | **+1.72%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.81% | **+1.63%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.27% | **+1.48%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.58% | **+1.42%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.88** / 初期 $100.00 (+33.88%)
- 確定: 880件 (Win 205 / Loss 261 / Flat 414) / skip 926件
- 成長率目線: 平均log +0.000332 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $133.88

## 4. Latest Market Context

- 更新: 2026-06-01T00:45:38.531151+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=73910.7
- Funnel: target 775 → liquid 133 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.1 >= 65=1, 4h RSI 80.3 >= 65=1, 4h RSI 76.2 >= 65=1, 4h RSI 75.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +173.07% | $22,557,876.87 |
| STG/USDT:USDT | +30.03% | $21,668,184.73 |
| H/USDT:USDT | +29.78% | $13,745,171.82 |
| LAB/USDT:USDT | +22.62% | $192,381,929.54 |
| ZORA/USDT:USDT | +21.80% | $1,777,883.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IBMSTOCK/USDT:USDT | below_1h_threshold | +4.95% | +4.60% |
| CTR/USDT:USDT | below_1h_threshold | +4.18% | +3.83% |
| ZEC/USDT:USDT | below_1h_threshold | +3.97% | +3.62% |
| PLAY/USDT:USDT | below_1h_threshold | +3.84% | +3.49% |
| VVV/USDT:USDT | below_1h_threshold | +2.80% | +2.45% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
