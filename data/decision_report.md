# Decision Report

- generated_at: 2026-06-06T17:36:28.890816+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5873**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5873, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.10% | **+0.33%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.66% | **+1.86%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.94% | **+1.36%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.58% | **+1.34%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.69% | **+0.62%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.21% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1014件 (Win 239 / Loss 313 / Flat 462) / skip 1420件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T17:36:25.657619+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=60767.5
- Funnel: target 771 → liquid 142 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.3 >= 65=1, 4h RSI 80.5 >= 65=1, 4h RSI 68.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +12.50% | $20,125,049.40 |
| SKYAI/USDT:USDT | +10.92% | $7,047,930.03 |
| MYX/USDT:USDT | +4.98% | $1,459,282.09 |
| BLUAI/USDT:USDT | +4.82% | $7,013,269.70 |
| SLX/USDT:USDT | +4.48% | $1,179,112.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +2.05% | +2.02% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.41% | +1.38% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +1.12% | +1.09% |
| ZEC/USDT:USDT | below_1h_threshold | +1.11% | +1.08% |
| ASTER/USDT:USDT | below_1h_threshold | +1.00% | +0.97% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
