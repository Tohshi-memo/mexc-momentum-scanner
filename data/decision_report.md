# Decision Report

- generated_at: 2026-05-24T08:54:22.587504+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4815**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4815, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=-0.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.38% | **-0.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.04% | **+0.03%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.00% | **+0.00%** |
| ASK | 20/20 | 100.0% | -0.21% | **-0.21%** |
| LIMIT_2PCT | 14/20 | 70.0% | -0.38% | **-0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.27% | **+0.89%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.15% | **+0.69%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.23% | **+0.62%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.35% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.99** / 初期 $100.00 (+21.99%)
- 確定: 621件 (Win 153 / Loss 197 / Flat 271) / skip 755件
- 成長率目線: 平均log +0.000320 / 幾何平均 +0.032% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $121.99

## 4. Latest Market Context

- 更新: 2026-05-24T08:54:14.369932+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=76787.9
- Funnel: target 764 → liquid 113 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.6 >= 65=1, 4h RSI 79.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +50.20% | $1,761,375.40 |
| PLUME/USDT:USDT | +22.26% | $2,052,758.75 |
| IN/USDT:USDT | +18.86% | $3,348,622.46 |
| GENIUS/USDT:USDT | +16.22% | $4,130,998.82 |
| BLUAI/USDT:USDT | +14.73% | $1,752,891.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +3.89% | +3.87% |
| AGT/USDT:USDT | below_1h_threshold | +3.11% | +3.09% |
| BSB/USDT:USDT | below_1h_threshold | +2.34% | +2.32% |
| BAN/USDT:USDT | below_1h_threshold | +1.97% | +1.95% |
| HYPE/USDT:USDT | below_1h_threshold | +1.65% | +1.63% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
