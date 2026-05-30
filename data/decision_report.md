# Decision Report

- generated_at: 2026-05-30T14:24:41.206325+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5130**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.69% / filled 20/20。**
- 全期間 MARKET基準: n=5130, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.69% | **+1.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.69% | **+1.69%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.68% | **+1.60%** |
| ASK | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_BB3S | 6/17 | 35.3% | +2.84% | **+1.00%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.94% | **+0.71%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.98% | **+0.79%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +0.39% | **+0.26%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.10% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.62** / 初期 $100.00 (+24.62%)
- 確定: 785件 (Win 183 / Loss 239 / Flat 363) / skip 906件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +5.01%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NFP/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $124.62

## 4. Latest Market Context

- 更新: 2026-05-30T14:24:38.987429+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=73920.6
- Funnel: target 773 → liquid 127 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +58.51% | $3,695,508.22 |
| LAB/USDT:USDT | +39.22% | $141,813,894.75 |
| STG/USDT:USDT | +34.28% | $2,059,236.14 |
| H/USDT:USDT | +33.95% | $6,924,437.58 |
| NFP/USDT:USDT | +27.12% | $3,686,871.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.00% | +3.84% |
| STG/USDT:USDT | below_1h_threshold | +3.24% | +3.08% |
| DYDX/USDT:USDT | below_1h_threshold | +2.74% | +2.59% |
| INJ/USDT:USDT | below_1h_threshold | +1.77% | +1.61% |
| WLD/USDT:USDT | below_1h_threshold | +1.55% | +1.39% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
