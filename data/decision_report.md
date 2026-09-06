# Decision Report

- generated_at: 2026-09-06T08:26:14.793440+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13805**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13805, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.07% | **+0.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_BB3S | 3/15 | 20.0% | +0.84% | **+0.17%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.18% | **+0.12%** |
| MARKET | 20/20 | 100.0% | +0.07% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +5.23% | **+3.14%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.94% | **+1.45%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.47% | **+1.03%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.14% | **+0.68%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.83% | **+0.66%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$856.28** / 初期 $100.00 (+756.28%)
- 確定: 5111件 (Win 1535 / Loss 1670 / Flat 1906) / skip 5255件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $856.28

## 4. Robust Adaptive DryRun ($100)

- 残高: **$192.89** / 初期 $100.00 (+92.89%)
- 確定: 2550件 (Win 713 / Loss 606 / Flat 1231) / skip 4666件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0131 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $192.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.11** / 初期 $100.00 (+20.11%)
- 確定: 2418件 (Win 721 / Loss 919 / Flat 778) / pending 3件 / skip 2855件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000207 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $120.11

## 6. Latest Market Context

- 更新: 2026-09-06T08:26:06.677134+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=79774.6
- Funnel: target 1054 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +48.57% | $151,505,551.19 |
| RAY/USDT:USDT | +33.39% | $3,220,956.83 |
| FLOCK/USDT:USDT | +30.05% | $1,262,982.44 |
| UAI/USDT:USDT | +20.01% | $12,834,544.10 |
| BASECAT/USDT:USDT | +18.84% | $2,288,867.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.70% | +4.68% |
| GRT/USDT:USDT | below_1h_threshold | +3.18% | +3.17% |
| FLOCK/USDT:USDT | below_1h_threshold | +1.96% | +1.94% |
| RAY/USDT:USDT | below_1h_threshold | +1.15% | +1.13% |
| ETHFI/USDT:USDT | below_1h_threshold | +0.66% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
