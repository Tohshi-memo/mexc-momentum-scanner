# Decision Report

- generated_at: 2026-06-06T01:55:12.827237+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5772**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5772, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |
| LIMIT_BB3S | 3/16 | 18.8% | -1.70% | **-0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.64% | **+1.85%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.55% | **+1.40%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.33% | **+1.28%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.69% | **+0.94%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.55% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1012件 (Win 239 / Loss 313 / Flat 460) / skip 1321件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T01:55:09.631875+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=61124.7
- Funnel: target 771 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +26.37% | $1,911,064.09 |
| HOME/USDT:USDT | +23.15% | $5,590,105.64 |
| ZEST/USDT:USDT | +21.09% | $2,482,438.35 |
| VVV/USDT:USDT | +19.36% | $8,769,359.24 |
| ZEC/USDT:USDT | +19.35% | $1,190,450,579.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIVER/USDT:USDT | below_1h_threshold | +3.24% | +3.43% |
| EPIC/USDT:USDT | below_1h_threshold | +3.10% | +3.29% |
| OPN/USDT:USDT | below_1h_threshold | +3.03% | +3.22% |
| MEME/USDT:USDT | below_1h_threshold | +2.79% | +2.97% |
| MYX/USDT:USDT | below_1h_threshold | +2.67% | +2.86% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
