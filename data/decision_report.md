# Decision Report

- generated_at: 2026-06-12T00:43:19.450148+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6432**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6432, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.27% | **-1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.97% | **+0.29%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.38% | **+0.15%** |
| LIMIT_BB3S | 4/18 | 22.2% | +0.53% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.48% | **+1.24%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.02% | **+1.21%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.88% | **+1.01%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.02% | **+0.66%** |

## 2. $100 Live Portfolio

- 残高: **$94.70** / 初期 $100.00 (-5.30%)
- 確定トレード: 15件 (TP 1 / SL 13 / EXP 1)
- 最新: XPL/USDT:USDT SL_HIT PnL -3.46% 残高後 $94.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.41** / 初期 $100.00 (+51.41%)
- 確定: 1327件 (Win 344 / Loss 427 / Flat 556) / skip 1666件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `MARKET_LONG` EXPIRED account -0.04% 残高後 $151.41

## 4. Latest Market Context

- 更新: 2026-06-12T00:43:11.453107+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=63652.4
- Funnel: target 782 → liquid 157 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.9 >= 65=1, 4h RSI 85.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +90.12% | $129,130,932.05 |
| ESPORTS/USDT:USDT | +81.14% | $25,397,424.23 |
| H/USDT:USDT | +23.99% | $35,196,496.20 |
| XPL/USDT:USDT | +19.14% | $2,962,603.45 |
| NAORIS/USDT:USDT | +18.50% | $1,458,299.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTR/USDT:USDT | below_1h_threshold | +4.20% | +4.11% |
| BSB/USDT:USDT | below_1h_threshold | +2.79% | +2.70% |
| XPL/USDT:USDT | below_1h_threshold | +2.19% | +2.10% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.99% | +1.90% |
| BILL/USDT:USDT | below_1h_threshold | +1.95% | +1.86% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
