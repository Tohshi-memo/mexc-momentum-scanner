# Decision Report

- generated_at: 2026-07-08T17:45:11.094120+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8495**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.67% / filled 20/20。**
- 全期間 MARKET基準: n=8495, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.67% | **+0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.11% | **+1.11%** |
| MARKET | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.94% | **+0.66%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.25% | **+0.50%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.94% | **+1.07%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.49% | **+0.27%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.30% | **+0.12%** |
| ASK_LONG | 20/20 | 100.0% | +0.09% | **+0.09%** |
| MARKET_LONG | 20/20 | 100.0% | +0.07% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$105.15** / 初期 $100.00 (+5.15%)
- 確定トレード: 78件 (TP 29 / SL 48 / EXP 1)
- 最新: VANRY/USDT:USDT SL_HIT PnL -4.00% 残高後 $105.15
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$321.89** / 初期 $100.00 (+221.89%)
- 確定: 2685件 (Win 851 / Loss 900 / Flat 934) / skip 2371件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.01% 残高後 $321.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 642件 (Win 152 / Loss 159 / Flat 331) / skip 1264件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0587 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.11

## 5. Latest Market Context

- 更新: 2026-07-08T17:45:01.172696+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=62248.7
- Funnel: target 851 → liquid 179 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +28.85% | $1,107,947.15 |
| TLM/USDT:USDT | +20.58% | $4,344,200.75 |
| VANRY/USDT:USDT | +17.59% | $5,906,043.27 |
| POWER/USDT:USDT | +13.22% | $2,282,767.01 |
| ALLO/USDT:USDT | +10.89% | $10,817,139.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_relative_strength | +5.10% | +4.84% |
| APE/USDT:USDT | below_relative_strength | +5.07% | +4.81% |
| BTW/USDT:USDT | below_1h_threshold | +3.63% | +3.37% |
| YFI/USDT:USDT | below_1h_threshold | +3.45% | +3.19% |
| VVV/USDT:USDT | below_1h_threshold | +2.48% | +2.22% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
