# Decision Report

- generated_at: 2026-06-01T00:50:53.683847+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5247**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5247, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.01% | **-1.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +4.39% | **+0.88%** |
| LIMIT_10PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_9PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_8PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_7PCT | 5/20 | 25.0% | -0.24% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.27% | **+2.04%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.67% | **+2.02%** |
| LIMIT_BB3S_LONG | 6/11 | 54.5% | +3.53% | **+1.93%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.90% | **+1.89%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.79% | **+1.68%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$134.91** / 初期 $100.00 (+34.91%)
- 確定: 882件 (Win 206 / Loss 261 / Flat 415) / skip 926件
- 成長率目線: 平均log +0.000339 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $134.91

## 4. Latest Market Context

- 更新: 2026-06-01T00:50:49.723669+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=73912.0
- Funnel: target 775 → liquid 133 → pre 50 → checked 50 → surge 5 → strict 0
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.9 >= 65=1, 4h RSI 80.6 >= 65=1, 4h RSI 76.5 >= 65=1, 4h RSI 74.7 >= 65=1, 4h RSI 87.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +176.21% | $22,890,576.46 |
| STG/USDT:USDT | +32.12% | $21,739,408.81 |
| H/USDT:USDT | +31.06% | $13,841,782.70 |
| LAB/USDT:USDT | +23.11% | $193,081,503.09 |
| HOME/USDT:USDT | +21.07% | $3,391,773.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CTR/USDT:USDT | below_1h_threshold | +4.13% | +3.78% |
| ZEC/USDT:USDT | below_1h_threshold | +3.83% | +3.48% |
| HOME/USDT:USDT | below_1h_threshold | +3.23% | +2.88% |
| PLAY/USDT:USDT | below_1h_threshold | +3.17% | +2.82% |
| WLD/USDT:USDT | below_1h_threshold | +2.97% | +2.62% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
