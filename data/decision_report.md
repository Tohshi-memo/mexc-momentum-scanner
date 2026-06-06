# Decision Report

- generated_at: 2026-06-06T18:51:08.208384+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5881**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5881, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.01% | **+0.01%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | -0.69% | **-0.07%** |
| LIMIT_BB3S | 3/15 | 20.0% | -1.80% | **-0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.80% | **+1.96%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.57% | **+1.80%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.55% | **+1.40%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.36% | **+1.16%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +1.31% | **+1.05%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.71** / 初期 $100.00 (+30.71%)
- 確定: 1016件 (Win 240 / Loss 314 / Flat 462) / skip 1426件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $130.71

## 4. Latest Market Context

- 更新: 2026-06-06T18:50:58.038460+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=60485.2
- Funnel: target 771 → liquid 142 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +28.70% | $1,326,469.23 |
| SKYAI/USDT:USDT | +20.81% | $12,012,737.15 |
| HOME/USDT:USDT | +11.37% | $10,398,452.27 |
| LAB/USDT:USDT | +8.55% | $44,603,159.34 |
| BSB/USDT:USDT | +8.13% | $4,116,427.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_1h_threshold | +4.32% | +4.43% |
| BABY/USDT:USDT | below_1h_threshold | +3.89% | +4.01% |
| FIDA/USDT:USDT | below_1h_threshold | +3.25% | +3.36% |
| GUA/USDT:USDT | below_1h_threshold | +2.46% | +2.58% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +2.44% | +2.56% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
