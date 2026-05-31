# Decision Report

- generated_at: 2026-05-31T15:41:03.606738+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5203**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5203, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.68% | **-1.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.25% | **+0.20%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.05% | **+0.04%** |
| LIMIT_BB3S | 5/14 | 35.7% | -1.07% | **-0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +8.00% | **+2.67%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.85% | **+1.85%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.35% | **+1.68%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.89% | **+1.47%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.77% | **+1.33%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.26** / 初期 $100.00 (+29.26%)
- 確定: 838件 (Win 194 / Loss 249 / Flat 395) / skip 926件
- 成長率目線: 平均log +0.000306 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.93% 残高後 $129.26

## 4. Latest Market Context

- 更新: 2026-05-31T15:40:59.923759+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=73675.4
- Funnel: target 773 → liquid 124 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.5 >= 65=1, 4h RSI 67.2 >= 65=1, 4h RSI 74.0 >= 65=1, 4h RSI 84.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +48.29% | $11,557,261.24 |
| AIA/USDT:USDT | +36.68% | $4,999,666.54 |
| STG/USDT:USDT | +34.01% | $5,086,455.02 |
| ALLO/USDT:USDT | +29.17% | $26,700,778.18 |
| PORTAL/USDT:USDT | +27.54% | $9,749,845.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +2.92% | +2.78% |
| UP/USDT:USDT | below_1h_threshold | +2.44% | +2.30% |
| VVV/USDT:USDT | below_1h_threshold | +2.31% | +2.17% |
| DASH/USDT:USDT | below_1h_threshold | +1.59% | +1.45% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.42% | +1.28% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
