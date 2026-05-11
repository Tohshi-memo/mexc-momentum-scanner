# Decision Report

- generated_at: 2026-05-11T03:42:50.834610+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4005**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.10% / filled 20/20。**
- 全期間 MARKET基準: n=4005, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+2.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.10% | **+2.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.10% | **+2.10%** |
| ASK | 20/20 | 100.0% | +2.03% | **+2.03%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.13% | **+1.81%** |
| LIMIT_BB3S | 6/12 | 50.0% | +2.96% | **+1.48%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.33% | **+0.86%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +1.58% | **+1.26%** |
| LIMIT_3PCT_LONG | 19/20 | 95.0% | +0.74% | **+0.70%** |
| LIMIT_ATR_LONG | 18/20 | 90.0% | +0.67% | **+0.60%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.61% | **+0.40%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.57** / 初期 $100.00 (+8.57%)
- 確定: 211件 (Win 53 / Loss 73 / Flat 85) / skip 355件
- 成長率目線: 平均log +0.000390 / 幾何平均 +0.039% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPG/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $108.57

## 4. Latest Market Context

- 更新: 2026-05-11T03:42:47.534624+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.60% price=80647.4
- Funnel: target 775 → liquid 179 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +32.20% | $9,970,042.50 |
| ALCH/USDT:USDT | +21.04% | $4,022,670.85 |
| TROLLSOL/USDT:USDT | +15.71% | $5,361,105.31 |
| FOLKS/USDT:USDT | +12.74% | $1,280,178.20 |
| OPG/USDT:USDT | +10.49% | $1,566,106.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAS/USDT:USDT | below_1h_threshold | +1.64% | +2.24% |
| KITE/USDT:USDT | below_1h_threshold | +0.95% | +1.55% |
| BAT/USDT:USDT | below_1h_threshold | +0.91% | +1.51% |
| OG/USDT:USDT | below_1h_threshold | +0.78% | +1.38% |
| US/USDT:USDT | below_1h_threshold | +0.77% | +1.37% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
