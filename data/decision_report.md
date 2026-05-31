# Decision Report

- generated_at: 2026-05-31T20:47:24.233464+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5225**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5225, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-2.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.52% | **-2.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +2.65% | **+1.06%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.54% | **+0.92%** |
| LIMIT_BB3S | 11/20 | 55.0% | +0.39% | **+0.22%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +4.38% | **+1.97%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +3.75% | **+1.69%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.95% | **+1.62%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.03% | **+1.62%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.16** / 初期 $100.00 (+31.16%)
- 確定: 860件 (Win 199 / Loss 255 / Flat 406) / skip 926件
- 成長率目線: 平均log +0.000315 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $131.16

## 4. Latest Market Context

- 更新: 2026-05-31T20:47:21.743160+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=73665.9
- Funnel: target 773 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +38.09% | $15,883,513.19 |
| PORTAL/USDT:USDT | +14.48% | $11,955,818.49 |
| BIANRENSHENG/USDT:USDT | +12.59% | $3,195,615.18 |
| ZORA/USDT:USDT | +12.47% | $1,424,975.87 |
| HOME/USDT:USDT | +11.94% | $2,665,290.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +3.08% | +2.89% |
| GRASS/USDT:USDT | below_1h_threshold | +2.30% | +2.11% |
| FET/USDT:USDT | below_1h_threshold | +2.24% | +2.04% |
| XLM/USDT:USDT | below_1h_threshold | +1.91% | +1.72% |
| LUNC/USDT:USDT | below_1h_threshold | +1.86% | +1.67% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
