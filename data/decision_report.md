# Decision Report

- generated_at: 2026-07-01T20:45:57.485047+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8013**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=8013, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.87% | **+0.87%** |
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.09% | **+0.77%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.91% | **+0.69%** |
| LIMIT_7PCT | 7/20 | 35.0% | +1.66% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.33% | **+0.53%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| ASK_LONG | 20/20 | 100.0% | +0.28% | **+0.28%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.36% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$273.71** / 初期 $100.00 (+173.71%)
- 確定: 2410件 (Win 737 / Loss 799 / Flat 874) / skip 2164件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $273.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.58** / 初期 $100.00 (+7.58%)
- 確定: 530件 (Win 135 / Loss 124 / Flat 271) / skip 894件
- 成長率目線: 平均log +0.000138 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0425 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $107.58

## 5. Latest Market Context

- 更新: 2026-07-01T20:45:51.152352+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=60021.6
- Funnel: target 825 → liquid 157 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.8 >= 65=1, 4h RSI 67.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TLM/USDT:USDT | +56.81% | $1,949,074.28 |
| LIT/USDT:USDT | +16.84% | $5,538,605.08 |
| NOM/USDT:USDT | +10.95% | $4,828,380.56 |
| RIF/USDT:USDT | +10.76% | $2,861,287.20 |
| H/USDT:USDT | +7.65% | $8,028,879.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASED/USDT:USDT | below_1h_threshold | +4.12% | +4.08% |
| LIT/USDT:USDT | below_1h_threshold | +4.00% | +3.96% |
| JUP/USDT:USDT | below_1h_threshold | +2.91% | +2.87% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.82% | +2.78% |
| BEAT/USDT:USDT | below_1h_threshold | +2.80% | +2.76% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
