# Decision Report

- generated_at: 2026-05-10T21:48:04.348624+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3992**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.36% / filled 20/20。**
- 全期間 MARKET基準: n=3992, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.36% | **+0.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +3.03% | **+1.21%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.44% | **+0.42%** |
| ASK | 20/20 | 100.0% | +0.37% | **+0.37%** |
| MARKET | 20/20 | 100.0% | +0.36% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 17/20 | 85.0% | +2.50% | **+2.13%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.86% | **+1.11%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.80% | **+0.76%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.05% | **+0.74%** |
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +0.81% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.80** / 初期 $100.00 (+8.80%)
- 確定: 202件 (Win 50 / Loss 68 / Flat 84) / skip 351件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $108.80

## 4. Latest Market Context

- 更新: 2026-05-10T21:48:01.026964+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=80812.7
- Funnel: target 769 → liquid 181 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +42.54% | $3,952,022.40 |
| ALCH/USDT:USDT | +20.55% | $3,237,908.44 |
| B/USDT:USDT | +13.94% | $2,395,629.53 |
| TROLLSOL/USDT:USDT | +13.68% | $4,462,477.00 |
| SUI/USDT:USDT | +12.37% | $731,099,317.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TROLLSOL/USDT:USDT | below_relative_strength | +5.04% | +4.89% |
| LAB/USDT:USDT | below_1h_threshold | +4.80% | +4.65% |
| FHE/USDT:USDT | below_1h_threshold | +3.74% | +3.59% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.65% | +2.50% |
| OG/USDT:USDT | below_1h_threshold | +2.42% | +2.27% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
