# Decision Report

- generated_at: 2026-06-02T03:30:09.986723+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5395**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.69% / filled 20/20。**
- 全期間 MARKET基準: n=5395, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 12/20 | 60.0% | +2.05% | **+1.23%** |
| ASK | 20/20 | 100.0% | +1.21% | **+1.21%** |
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.97% | **+0.44%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.45% | **+0.31%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.17% | **+0.22%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.05% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$96.63** / 初期 $100.00 (-3.37%)
- 確定トレード: 84件 (TP 24 / SL 57 / EXP 3)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.63
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.76** / 初期 $100.00 (+31.76%)
- 確定: 908件 (Win 211 / Loss 272 / Flat 425) / skip 1048件
- 成長率目線: 平均log +0.000304 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $131.76

## 4. Latest Market Context

- 更新: 2026-06-02T03:30:07.144767+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=70943.2
- Funnel: target 776 → liquid 146 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +22.85% | $10,814,045.69 |
| RIF/USDT:USDT | +20.97% | $1,196,911.40 |
| LAB/USDT:USDT | +20.36% | $197,494,178.02 |
| WLD/USDT:USDT | +17.34% | $136,395,623.78 |
| SKYAI/USDT:USDT | +16.35% | $3,943,664.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +4.89% | +4.71% |
| LIT/USDT:USDT | below_1h_threshold | +4.78% | +4.61% |
| LAB/USDT:USDT | below_1h_threshold | +3.94% | +3.76% |
| EIGEN/USDT:USDT | below_1h_threshold | +3.87% | +3.70% |
| WLD/USDT:USDT | below_1h_threshold | +3.48% | +3.30% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
