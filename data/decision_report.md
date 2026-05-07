# Decision Report

- generated_at: 2026-05-07T00:17:30.900209+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3511**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3511, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.10% | **+0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.98% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.10% | **+0.10%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.07% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +3.49% | **+2.10%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.25% | **+1.12%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.92% | **+0.69%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.60% | **+0.42%** |
| ASK_LONG | 20/20 | 100.0% | +0.35% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$97.52** / 初期 $100.00 (-2.48%)
- 確定: 10件 (Win 0 / Loss 5 / Flat 5) / skip 62件
- 成長率目線: 平均log -0.002506 / 幾何平均 -0.250% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ORCA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $97.52

## 4. Latest Market Context

- 更新: 2026-05-07T00:17:25.786541+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=81342.2
- Funnel: target 765 → liquid 186 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEREBRO/USDT:USDT | +20.32% | $1,735,042.73 |
| PLAY/USDT:USDT | +20.26% | $18,159,297.26 |
| BILL/USDT:USDT | +13.45% | $10,236,972.43 |
| LAB/USDT:USDT | +11.47% | $249,817,539.06 |
| FHE/USDT:USDT | +10.20% | $16,621,550.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKT/USDT:USDT | below_1h_threshold | +3.70% | +3.76% |
| TAG/USDT:USDT | below_1h_threshold | +2.12% | +2.18% |
| VVV/USDT:USDT | below_1h_threshold | +1.57% | +1.63% |
| UB/USDT:USDT | below_1h_threshold | +1.20% | +1.25% |
| ARB/USDT:USDT | below_1h_threshold | +0.96% | +1.02% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
