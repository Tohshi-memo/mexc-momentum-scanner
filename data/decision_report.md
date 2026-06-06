# Decision Report

- generated_at: 2026-06-06T19:01:36.795546+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5884**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5884, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -0.98% | **-0.20%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |
| LIMIT_1PCT | 20/20 | 100.0% | -0.59% | **-0.59%** |
| LIMIT_ATR | 14/20 | 70.0% | -1.07% | **-0.75%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.93% | **+1.76%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.79% | **+1.07%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.96% | **+0.82%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.06% | **+0.74%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$132.02** / 初期 $100.00 (+32.02%)
- 確定: 1019件 (Win 241 / Loss 314 / Flat 464) / skip 1426件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $132.02

## 4. Latest Market Context

- 更新: 2026-06-06T19:01:34.543392+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=60596.5
- Funnel: target 771 → liquid 133 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +27.76% | $1,408,255.81 |
| SKYAI/USDT:USDT | +21.12% | $12,424,881.23 |
| LAB/USDT:USDT | +20.69% | $40,357,078.85 |
| HOME/USDT:USDT | +11.56% | $10,422,817.92 |
| BLUAI/USDT:USDT | +10.56% | $7,131,354.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.15% | +2.17% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.11% | +1.13% |
| BLUAI/USDT:USDT | below_1h_threshold | +0.94% | +0.96% |
| LAB/USDT:USDT | below_1h_threshold | +0.93% | +0.94% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.75% | +0.76% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
