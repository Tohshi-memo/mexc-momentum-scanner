# Decision Report

- generated_at: 2026-06-06T18:45:25.295055+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5880**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5880, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.06% | **+0.06%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | -0.69% | **-0.07%** |
| LIMIT_BB3S | 2/15 | 13.3% | -2.54% | **-0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +3.07% | **+2.00%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.95% | **+1.66%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.40% | **+1.56%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.24% | **+1.18%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +1.31% | **+1.05%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.37** / 初期 $100.00 (+31.37%)
- 確定: 1015件 (Win 240 / Loss 313 / Flat 462) / skip 1426件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $131.37

## 4. Latest Market Context

- 更新: 2026-06-06T18:45:15.784134+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=60579.9
- Funnel: target 771 → liquid 142 → pre 50 → checked 50 → surge 5 → strict 4
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +23.85% | $11,363,719.45 |
| FIDA/USDT:USDT | +20.59% | $1,258,147.38 |
| HOME/USDT:USDT | +11.64% | $10,355,153.30 |
| LAB/USDT:USDT | +9.29% | $44,380,150.22 |
| BLUAI/USDT:USDT | +8.75% | $7,133,166.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_1h_threshold | +4.59% | +4.55% |
| BABY/USDT:USDT | below_1h_threshold | +2.82% | +2.77% |
| BLUAI/USDT:USDT | below_1h_threshold | +2.57% | +2.53% |
| VELVET/USDT:USDT | below_1h_threshold | +1.92% | +1.88% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +1.77% | +1.72% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
