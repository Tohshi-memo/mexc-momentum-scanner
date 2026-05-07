# Decision Report

- generated_at: 2026-05-07T06:02:44.597772+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3575**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3575, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.73% | **-0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.56% | **+0.53%** |
| ASK | 20/20 | 100.0% | +0.50% | **+0.50%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_BB3S | 5/16 | 31.2% | +0.49% | **+0.15%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.32% | **+1.19%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +1.54% | **+1.03%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.97% | **+0.53%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.73% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.24** / 初期 $100.00 (+7.24%)
- 確定: 69件 (Win 26 / Loss 26 / Flat 17) / skip 67件
- 成長率目線: 平均log +0.001013 / 幾何平均 +0.101% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $107.24

## 4. Latest Market Context

- 更新: 2026-05-07T06:02:41.961164+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=81022.9
- Funnel: target 770 → liquid 185 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +225.22% | $1,729,267.25 |
| B3/USDT:USDT | +96.43% | $9,444,049.48 |
| DOGS/USDT:USDT | +73.11% | $11,822,583.84 |
| PENGUIN/USDT:USDT | +51.79% | $1,381,513.65 |
| FHE/USDT:USDT | +24.74% | $16,689,579.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +4.16% | +4.19% |
| IO/USDT:USDT | below_1h_threshold | +2.21% | +2.24% |
| BILL/USDT:USDT | below_1h_threshold | +1.38% | +1.41% |
| BRETT/USDT:USDT | below_1h_threshold | +0.84% | +0.87% |
| VVV/USDT:USDT | below_1h_threshold | +0.66% | +0.69% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
