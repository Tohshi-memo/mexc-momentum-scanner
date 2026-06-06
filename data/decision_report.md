# Decision Report

- generated_at: 2026-06-06T18:57:03.205600+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5883**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5883, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | -1.80% | **-0.27%** |
| LIMIT_1PCT | 20/20 | 100.0% | -0.54% | **-0.54%** |
| LIMIT_BB3S | 4/16 | 25.0% | -2.35% | **-0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.93% | **+1.76%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.79% | **+1.07%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.19% | **+1.07%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.40% | **+1.05%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$132.02** / 初期 $100.00 (+32.02%)
- 確定: 1018件 (Win 241 / Loss 314 / Flat 463) / skip 1426件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $132.02

## 4. Latest Market Context

- 更新: 2026-06-06T18:56:54.938018+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=60611.3
- Funnel: target 771 → liquid 142 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +27.98% | $1,392,432.21 |
| SKYAI/USDT:USDT | +20.47% | $12,351,082.71 |
| LAB/USDT:USDT | +14.80% | $45,288,183.17 |
| HOME/USDT:USDT | +13.27% | $10,429,531.43 |
| BLUAI/USDT:USDT | +8.99% | $7,139,280.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BABY/USDT:USDT | below_1h_threshold | +4.63% | +4.54% |
| BSB/USDT:USDT | below_1h_threshold | +3.74% | +3.65% |
| BLUAI/USDT:USDT | below_1h_threshold | +2.90% | +2.80% |
| FIDA/USDT:USDT | below_1h_threshold | +2.71% | +2.62% |
| GUA/USDT:USDT | below_1h_threshold | +2.60% | +2.51% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
