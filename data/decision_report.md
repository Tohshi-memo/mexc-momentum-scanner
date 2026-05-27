# Decision Report

- generated_at: 2026-05-27T01:54:27.225342+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4914**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4914, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=-0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.06% | **-0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.88% | **+0.19%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| ASK | 20/20 | 100.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.70% | **+1.10%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.16% | **+1.04%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.19% | **+0.65%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.00% | **+0.65%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.70% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 65件 (TP 18 / SL 44 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.36** / 初期 $100.00 (+29.36%)
- 確定: 679件 (Win 172 / Loss 216 / Flat 291) / skip 796件
- 成長率目線: 平均log +0.000379 / 幾何平均 +0.038% per trade / maxDD +4.72%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $129.36

## 4. Latest Market Context

- 更新: 2026-05-27T01:54:22.581835+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=75921.2
- Funnel: target 770 → liquid 137 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUNC/USDT:USDT | +11.11% | $7,310,821.16 |
| REQ/USDT:USDT | +10.88% | $1,095,230.34 |
| PLAY/USDT:USDT | +10.07% | $7,772,237.35 |
| GUA/USDT:USDT | +9.96% | $3,088,057.04 |
| MUSTOCK/USDT:USDT | +8.09% | $28,579,086.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.85% | +4.03% |
| PLAY/USDT:USDT | below_1h_threshold | +3.61% | +3.79% |
| UB/USDT:USDT | below_1h_threshold | +2.31% | +2.50% |
| DRIFT/USDT:USDT | below_1h_threshold | +2.27% | +2.45% |
| PHA/USDT:USDT | below_1h_threshold | +2.08% | +2.27% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
